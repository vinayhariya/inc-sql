from database import SessionLocal, engine, Base
from crud import create_user, get_user, get_users, update_user, delete_user

def init_db():
    Base.metadata.create_all(bind=engine)

def main():
    print("Initializing the database...")
    init_db()
    print("Database initialized")

    while True:
        print("\n==== USER MANAGEMENT MENU ====")
        print("1. Create User")
        print("2. Get User by ID")
        print("3. Get All Users")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")

        choice = input("Enter your choice: ")

        session = SessionLocal()

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            user = create_user(session, name, email)
            print(f"User created with ID: {user.id}")

        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            user = get_user(session, user_id)
            if user:
                print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
            else:
                print("User not found")

        elif choice == "3":
            users = get_users(session)
            if users:
                for user in users:
                    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
            else:
                print("No users found")

        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            name = input("Enter new name (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")

            user = update_user(session, user_id, name=name or None, email=email or None)
            if user:
                print("User updated successfully")
            else:
                print("User not found")

        elif choice == "5":
            user_id = int(input("Enter user ID: "))
            user = delete_user(session, user_id)
            if user:
                print("User deleted successfully")
            else:
                print("User not found")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")

    engine.drop()



if __name__ == "__main__":
    main()