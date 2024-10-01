from flask import Flask, request, jsonify, render_template, redirect, url_for
import google.generativeai as genai
import requests
import json
import os
from PIL import Image
import pyzbar.pyzbar as pyzbar

app = Flask(__name__)
# Configure the GenAI with your API key
genai.configure(api_key="AIzaSyApoKjsDAPW7YkWKzVlXoqTAkfENWQD1AA")

# Instantiate the Gemini AI model with the specified configuration
model = genai.GenerativeModel('gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})

# Function to generate detailed product analysis using Gemini AI
def get_gemini_analysis(product_name):
    prompt = f"""
    Analyze the following product:
    Product Name: {product_name}

    Provide the accurate information in this JSON format:
    {{
        "Nutrients": {{
            "Total Fat": int,
            "Saturated Fat": int,
            "Cholesterol": int,
            "Sodium": int,
            "Total Carbohydrates": int,
            "Dietary Fiber": int,
            "Sugars": int,
            "Protein": int
        }},
        "Allergies": [str],
        "FSSAI Approved": str,
        "Label Claims": [str],
        "Health Analysis": {{
            "Nutritional Analysis": str,
            "Processing and Nutrient Deficit": str,
            "Harmful Ingredients": str,
            "Diabetes Friendly": str,
            "Allergies Friendly": str,
            "Vegan": str,
            "Misleading Claims": str,
            "Similar Healthy Product": str
        }}
    }}
    """
    try:
        # Generate content using the model
        response = model.generate_content(prompt)
        response_text = response.text

        # Print the raw response for debugging
        print("Raw response:", response_text)

        # Parse the JSON response
        analysis = json.loads(response_text)

        # Validate the response structure
        if not isinstance(analysis, dict):
            return {"error": "Invalid response format from Gemini API."}

        # Ensure required fields are present
        required_fields = ["Nutrients", "Allergies", "FSSAI Approved", "Label Claims", "Health Analysis"]
        for field in required_fields:
            if field not in analysis:
                analysis[field] = "Not Available"

        # Return the analysis
        return analysis

    except json.JSONDecodeError:
        print("Error parsing JSON response.")
        return {"error": "Failed to decode JSON response from Gemini API."}
    except Exception as e:
        print(f"Error fetching Gemini analysis: {e}")
        return {"error": "An error occurred while fetching the analysis from Gemini."}

def ai_get_gemini_analysis(product_name):
    prompt = f"""
    Analyze the following product:
    Product Name: {product_name}

    Is this a consumable product? If yes,Provide the accurate information in this JSON format:
    {{
                "is_consumable": bool,
        "Product Info":{{
                 'Product Name': str,
                'Quantity': str,
                'Brand': str,
                'Categories': str,
                'Ingredients in the product': str,
                }},
        "Nutrients": {{
            "Total Fat": int,
            "Saturated Fat": int,
            "Cholesterol": int,
            "Sodium": int,
            "Total Carbohydrates": int,
            "Dietary Fiber": int,
            "Sugars": int,
            "Protein": int
        }},
        "Allergies": [str],
        "FSSAI Approved": str,
        "Label Claims": [str],
        "Health Analysis": {{
            "Nutritional Analysis": str,
            "Processing and Nutrient Deficit": str,
            "Harmful Ingredients": str,
            "Diabetes Friendly": str,
            "Allergies Friendly": str,
            "Vegan": str,
            "Misleading Claims": str,
            "Similar Healthy Product": str
        }}
    }}
    """
    try:
        # Generate content using the model
        response = model.generate_content(prompt)
        response_text = response.text

        # Print the raw response for debugging
        print("Raw response:", response_text)

        # Parse the JSON response
        analysis = json.loads(response_text)

        # Validate the response structure
        if not isinstance(analysis, dict):
            return {"error": "Invalid response format from Gemini API."}

        # Ensure required fields are present
        required_fields = ["Product Info","Nutrients", "Allergies", "FSSAI Approved", "Label Claims", "Health Analysis"]
        for field in required_fields:
            if field not in analysis:
                analysis[field] = "Not Available"

        # Return the analysis
        return analysis

    except json.JSONDecodeError:
        print("Error parsing JSON response.")
        return {"error": "Failed to decode JSON response from Gemini API."}
    except Exception as e:
        print(f"Error fetching Gemini analysis: {e}")
        return {"error": "An error occurred while fetching the analysis from Gemini."}

# Function to generate analysis for consumable products
def generate_gemini_analysis(product_name):
    prompt = f"""
    Analyze the following product:
    Product Name: {product_name}

    Is this a consumable product? If yes, suggest a healthier alternative in JSON format:
    {{
        "is_consumable": bool,
        "healthier_choice": str,
        "reason": str,
    }}
    """
    try:
        response = model.generate_content(prompt)
        response_text = response.text
        analysis = json.loads(response_text)
        return analysis
    except json.JSONDecodeError:
        return {"error": "Failed to decode JSON response from Gemini API."}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# Function to extract product information
def get_product_info(identifier):
    if identifier.isdigit():
        url = f"https://world.openfoodfacts.org/api/v0/product/{identifier}.json"
    else:
        search_url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={identifier}&search_simple=1&action=process&json=1"
        search_response = requests.get(search_url)
        if search_response.status_code == 200:
            search_data = search_response.json()
            if search_data.get('count', 0) > 0:
                product_code = search_data['products'][0].get('code')
                if product_code:
                    url = f"https://world.openfoodfacts.org/api/v0/product/{product_code}.json"
                else:
                    return {"error": "No product code found for this product name"}
            else:
                return {"error": "Product not found"}
        else:
            return {"error": "Failed to search for the product"}

    response = requests.get(url)
    if response.status_code == 200:
        product_data = response.json()
        if product_data.get('status') == 1:
            product_info = product_data.get('product', {})
            analysis = {
                'Product Name': product_info.get('product_name', 'Unknown'),
                'Quantity': product_info.get('quantity', 'Not Available'),
                'Brand': product_info.get('brands', 'Unknown'),
                'Categories': product_info.get('categories', 'Not Specified'),
                'Ingredients': product_info.get('ingredients_text', 'Not Available'),
                'Product Image': product_info.get('image_front_url', '/static/placeholder.png'),
            }
            return analysis
        else:
            return {"error": "Product not found"}
    else:
        return {"error": "Failed to fetch product information"}

# Function to extract barcode from an image
def extract_barcode_from_image(image_file):
    try:
        temp_path = os.path.join('temp', image_file.filename)
        image_file.save(temp_path)
        image = Image.open(temp_path)
        decoded_objects = pyzbar.decode(image)
        barcodes = [obj.data.decode('utf-8') for obj in decoded_objects]
        os.remove(temp_path)
        return barcodes[0] if barcodes else None
    except Exception as e:
        print(f"Error extracting barcode from image: {e}")
        return None
    


    

# Route for chatbot functionality
@app.route('/check-product', methods=['POST'])
def check_product_route():
    data = request.json
    product_name = data.get('product_name')

    if not product_name:
        return jsonify({"error": "No product name provided"}), 400

    # Generate analysis using the Gemini AI
    gemini_response = generate_gemini_analysis(product_name)

    # Check if the product is consumable or not and return the appropriate response
    if not gemini_response.get('is_consumable', False):
        return jsonify({
            "product_name": product_name,
            "consumable": False,
            "message": gemini_response.get('reason', 'Not a consumable product.'),

        })

    return jsonify({
        "product_name": product_name,
        "consumable": True,
        "healthier_choice": gemini_response.get('healthier_choice'),
        "reason": gemini_response.get('reason'),

        
        
    })

# # Existing routes
# @app.route('/')
# def home():
#     return render_template('home.html')


@app.route('/manual-entry', methods=['GET', 'POST'])
def manual_entry():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        search_with_ai = request.form.get('search_with_ai', 'false')

        if search_with_ai == 'true':
            # User chose to search with AI
            gemini_result = ai_get_gemini_analysis(product_name)
            return render_template('result.html', result=gemini_result)
        else:
            # Regular flow
            result = get_product_info(product_name)
            if 'error' in result:
                if result['error'] == "Product not found":
                    # Render the template with a flag to show the popup
                    return render_template('manual_entry.html', error=result['error'], show_popup=True,
                                           product_name=product_name)
                else:
                    # Render template with error message without popup
                    return render_template('manual_entry.html', error=result['error'])
            gemini_result = get_gemini_analysis(product_name)
            return render_template('result.html', result={**result, **gemini_result})
    return render_template('manual_entry.html')



@app.route('/speech-to-text', methods=['GET', 'POST'])
def speech_to_text():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        search_with_ai = request.form.get('search_with_ai', 'false')

        if search_with_ai == 'true':
            # If user chooses to search with AI
            gemini_result = ai_get_gemini_analysis(product_name)
            return render_template('result.html', result=gemini_result)
        else:
            # Search for the product in the database
            result = get_product_info(product_name)
            if 'error' in result:
                if result['error'] == "Product not found":
                    # Show popup with manual entry option
                    return render_template('speech_to_text.html', error=result['error'], show_popup=True,
                                           product_name=product_name)
                else:
                    # Render template with error message for other errors
                    return render_template('speech_to_text.html', error=result['error'])
            # If product is found, display its analysis
            gemini_result = get_gemini_analysis(product_name)
            return render_template('result.html', result={**result, **gemini_result})

    # Render the initial form for GET requests
    return render_template('speech_to_text.html')




@app.route('/barcode', methods=['GET', 'POST'])
def barcode():
    if request.method == 'POST':
        barcode_file = request.files.get('barcode_file')
        search_with_ai = request.form.get('search_with_ai', 'false')
        manual_entry = request.form.get('manual_entry', 'false')

        if manual_entry == 'true':
            return redirect(url_for('manual_entry'))

        barcode_data = extract_barcode_from_image(barcode_file)
        if barcode_data:
            if search_with_ai == 'true':
                gemini_result = ai_get_gemini_analysis(barcode_data)
                return render_template('result.html', result=gemini_result)
            else:
                result = get_product_info(barcode_data)
                if 'error' in result:
                    if result['error'] == "Product not found":
                        return render_template('barcode.html', error=result['error'], show_popup=True)
                    else:
                        return render_template('barcode.html', error=result['error'])
                gemini_result = get_gemini_analysis(result['Product Name'])
                return render_template('result.html', result={**result, **gemini_result})
        else:
            # Show popup to allow manual entry
            return render_template('barcode.html', error="Unable to read barcode from the image.", allow_manual=True)
    return render_template('barcode.html')



# New chatbot route
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')


@app.route('/')
def hii():
    return render_template('hii.html') 

if __name__ == '__main__':
    if not os.path.exists('temp'):
        os.makedirs('temp')
    app.run(debug=True)
    
    
    
   