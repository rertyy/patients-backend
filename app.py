from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=10000)
    # app.run(host="0.0.0.0", port=5000, debug=True)
