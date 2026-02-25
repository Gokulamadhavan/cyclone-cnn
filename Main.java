// File: Main.java

// A simple Java program to manage a small library
class Book {
    String title;
    String author;
    int year;

    // Constructor
    Book(String title, String author, int year) {
        this.title = title;
        this.author = author;
        this.year = year;
    }

    // Display book details
    void displayInfo() {
        System.out.println(title + " by " + author + " (" + year + ")");
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an array of books
        Book[] library = {
            new Book("1984", "George Orwell", 1949),
            new Book("The Alchemist", "Paulo Coelho", 1988),
            new Book("Clean Code", "Robert C. Martin", 2008)
        };

        // Print all books
        System.out.println("Library collection:");
        for (Book book : library) {
            book.displayInfo();
        }

        // Add a new book dynamically
        Book newBook = new Book("Java: The Complete Reference", "Herbert Schildt", 2024);
        System.out.println("\nAdding a new book:");
        newBook.displayInfo();
    }
}
