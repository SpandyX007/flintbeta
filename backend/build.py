def main():
    print("Running build command...")
    with open("requirements.txt", "w") as f:
        f.write("BUILD_COMMAND")
 
if __name__ == "__main__":
    main()