
# Project 1

## Description
NumbersView is a Django project that implements a view to fetch numbers from various test servers, maintaining a window of the last 10 fetched numbers for each type (p, f, e, or r). It calculates the average of the numbers in the window and ensures a response time within 500 milliseconds.

## Setup Instructions
1. Ensure Django is installed. If not, install it using pip:

2. Clone the project repository from GitHub or download the project zip file.

3. Start the Django development server:

4. Visit `http://localhost:9876/numbers/<type>/` in your web browser, replacing `<type>` with p, f, e, or r to fetch numbers of the specified type.

## Usage
- Navigate to `http://localhost:9876/numbers/<type>/` to fetch numbers.
- The response includes:
- Fetched numbers.
- Previous state of the window.
- Current state of the window.
- Average of the numbers in the window.

---

## Output Screenshots

### Output for http://localhost:9878/numbers/e
<div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; max-width: 600px;">
    <p><strong>Output for http://localhost:9878/numbers/e</strong></p>
    <img src="https://github.com/deekshith-31123/2100031123/assets/109582945/530ca7f2-9c38-4b7d-a4b2-8caa212cdf53" alt="Output for e" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>

### Output for http://localhost:9878/numbers/f
<div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; max-width: 600px;">
    <p><strong>Output for http://localhost:9878/numbers/f</strong></p>
    <img src="https://github.com/deekshith-31123/2100031123/assets/109582945/0e6d0d57-f5f4-4369-840c-4a3fd611014f" alt="Output for f" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>

### Output for http://localhost:9878/numbers/p
<div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; max-width: 600px;">
    <p><strong>Output for http://localhost:9878/numbers/p</strong></p>
    <img src="https://github.com/deekshith-31123/2100031123/assets/109582945/324668e2-9426-462e-869e-ddb5ce30d2cf" alt="Output for p" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>

### Output for http://localhost:9878/numbers/r
<div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; max-width: 600px;">
    <p><strong>Output for http://localhost:9878/numbers/r</strong></p>
    <img src="https://github.com/deekshith-31123/2100031123/assets/109582945/686fd9a6-2a89-40f8-922f-f607fa8c8e1e" alt="Output for r" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>


# Project 2

## Description
This Django project serves as a web application to fetch and display top products from an external API based on company and category. It includes modularized components for better organization and maintainability.

## Requirements
- Python 3.x
- Django 3.x
- Dependencies listed in `requirements.txt`

## Installation
1. Clone the repository:

2. Install dependencies:
3. Set up configuration:
- Add `BEARER_TOKEN` to `config.py` for API authentication.

4. Run migrations (if using a database):

## Usage
1. Start the Django development server:

2. Access the application in your web browser at `http://localhost:9876/`.

3. Use the provided API endpoints to fetch top products based on company and category:
- Parameters:
  - `top`: Number of products to fetch (default: 10).
  - `minPrice`, `maxPrice`: Price range filters.
  - `sortBy`: Sorting parameter (default: 'price').
  - `order`: Sorting order ('asc' or 'desc', default: 'asc').

## Project Structure
- `api_client.py`: Functions to communicate with the external API and fetch products.
- `product_handler.py`: Handles processing and pagination of products from the API.
- `views.py`: Django view functions to serve web requests and return JSON responses.

## Documentation
- Further documentation can be found in the project's source code or documentation folder.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Credits
- Project maintained by Praveen (2100030888).
- External APIs used for product data retrieval (list any relevant external sources).

## Support
For any issues or inquiries, please contact Praveen via email at praveen@example.com.

## Acknowledgements
- Special thanks to the Django community for their continuous support and contributions.


## Output Screenshots


### Output for http://localhost:9878/companies/AMZ/categories/TV/products?top=10&minPrice=1&maxPrice=10000

<div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; max-width: 600px;">
    <p><strong>Output for http://localhost:9878/companies/AMZ/categories/TV/products?top=10&minPrice=1&maxPrice=10000</strong></p>
    <img src="https://github.com/deekshith-31123/2100031123/assets/109582945/c656a7f9-dc35-4061-8e3d-30cf88607758" alt="Output image 1" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>

<div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; max-width: 600px;">
    <img src="https://github.com/deekshith-31123/2100031123/assets/109582945/65b2ae72-64be-4a7a-8052-fb1bb342c87d" alt="Output image 2" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>

<div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; max-width: 600px;">
    <img src="https://github.com/deekshith-31123/2100031123/assets/109582945/cf98e9f3-6e2b-4b71-acc1-f7fb07ed7e53" alt="Output image 3" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>

