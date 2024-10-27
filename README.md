

# E-commerce Django Application

This is an e-commerce web application built with Django. The application provides functionalities for users to browse products, register and login, add products to a cart, checkout, and view order history. It also includes an admin panel for managing the application.

## Features

- **Product Listing**: Users can view a list of products.
- **Product Detail**: Users can view detailed information about a product.
- **User Registration**: Users can create an account to make purchases.
- **User Authentication**: Users can log in and log out.
- **Cart Management**: Users can add products to their cart, update quantities, and remove items.
- **Checkout**: Users can proceed to checkout and place orders.
- **Order History**: Users can view their order history.
- **Admin Panel**: Admins can manage products, orders, and users.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Open a web browser and go to `http://127.0.0.1:8000` to view the application.
   - Go to `http://127.0.0.1:8000/admin` to access the admin panel.

## Usage

### Product Listing
- Users can view all available products on the homepage.

### Product Detail
- Users can click on a product to view its details.

### User Registration
- Users can register by navigating to the registration page.

### User Authentication
- Registered users can log in and log out.

### Cart Management
- Users can add products to their cart from the product detail page.
- Users can view their cart, update quantities, and remove items from the cart detail page.

### Checkout
- Users can proceed to checkout from the cart detail page.
- Upon successful checkout, the cart is cleared, and the order is saved.

### Order History
- Users can view their past orders on the order history page.

### Admin Panel
- Admins can manage products, orders, and users through the admin panel.

## Directory Structure

```
your-repo-name/
├── shop/
│   ├── migrations/
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   └── register.html
│   │   ├── shop/
│   │   │   ├── cart_detail.html
│   │   │   ├── checkout.html
│   │   │   ├── order_history.html
│   │   │   ├── product_detail.html
│   │   │   └── product_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── ecommerce/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Models

### Product
- **Fields**: name, description, price, stock, created_at, updated_at

### Cart
- **Fields**: user, created_at, updated_at

### CartItem
- **Fields**: cart, product, quantity, created_at, updated_at

### Order
- **Fields**: user, created_at, updated_at
- **Related Models**: OrderItem

### OrderItem
- **Fields**: order, product, quantity, price

## Forms

### UserRegistrationForm
- Custom user registration form with email field.

### CartItemForm
- Form for updating cart item quantities.

## URLs

- **`/`**: Product listing
- **`/product/<int:product_id>/`**: Product detail
- **`/register/`**: User registration
- **`/login/`**: User login
- **`/logout/`**: User logout
- **`/add_to_cart/<int:product_id>/`**: Add product to cart
- **`/cart_detail/`**: View cart details
- **`/remove_from_cart/<int:item_id>/`**: Remove item from cart
- **`/update_cart/`**: Update cart item quantities
- **`/checkout/`**: Checkout
- **`/order_history/`**: View order history

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Contact

For any questions or suggestions, feel free to contact the project maintainer at `theycallmejoly@outlook.com`.
