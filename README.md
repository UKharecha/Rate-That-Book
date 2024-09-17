# 📚 Rate That Book

Welcome to **Rate That Book**! This project allows users to sign up, log in, and share their thoughts on their favorite books. Users can explore other people's reviews, manage their own profiles, and engage with the books they love. 📖

## 🚀 Features

- 📝 **User Registration & Login**: Sign up and log in securely to create your own profile.
- 📚 **Add, Update, and Delete Books**: Manage your collection of books.
- 🌟 **Post Reviews**: Share your thoughts about books, give ratings, and update or delete your reviews.
- 👀 **View All Reviews**: Browse reviews posted by others for each book.

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Authentication**: JWT-based authentication

## 📑 API Endpoints

### Authentication

- `POST /user/login` – User login

### Books

- `GET /book/getall` – View all books
- `POST /book/addone` – Add a new book
- `PUT /book/update/<id>` – Update a book
- `DELETE /book/delete/<id>` – Delete a book

### Users

- `GET /user/getall` – View all reviews for a specific book
- `POST /user/addone` – Add a review for a book
- `PUT /user/update/<id>` – Update a review
- `DELETE /user/delete/<id>` – Delete a review

## 🔧 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/ukharecha/rate-that-book.git
```
```bash
cd rate-that-book
```

### Step 2: Create a Virtual Environment and Install Dependencies
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
flask run
```

## 🧑‍💻 Contribution Guidelines

We welcome contributions! Here’s how you can get involved:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m 'Add a new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## 🐛 Bug Reports & 📝 Feature Requests

If you encounter any bugs or have a feature request, feel free to open an issue in this repository.


