import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        """Set up the test client for the Flask application."""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_page(self):
        """Test the index page loads successfully."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Flask App", response.data)

    def test_about_page(self):
        """Test the about page loads successfully."""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Us", response.data)

    def test_contact_page_get(self):
        """Test the contact page loads successfully with GET."""
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Contact Us", response.data)

    def test_contact_page_post(self):
        """Test the contact page form submission."""
        response = self.client.post('/contact', data={
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Hello, this is a test message.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Thank you, USER! Your message has been received.", response.data)

    def test_404_page(self):
        """Test a non-existing route returns a 404 status."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
