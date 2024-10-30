hero_content = """
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Poppins', sans-serif;
            flex-direction: column;
        }
        .marquee {
            width: 100%;
            background: #f0f0f0; 
            padding: 10px 0;
            text-align: center;
            font-weight: 600;
            color: #333;
            position: absolute;
            top: 0;
            z-index: 1;
        }
        .form-container {
            display: flex;
            align-items: center;
            margin-top: 80px;
        }
        h1 {
            font-size: 24px;
            margin: 0;
            text-align: center;
            font-weight: 600;
        }
        input[type="text"] {
            padding: 10px;
            font-size: 16px;
            width: 400px;
            margin-right: 10px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="marquee">
        <marquee behavior="scroll" direction="left" scrollamount="12">
        We may take up to a minute to resolve your query!; 
        </marquee>
    </div>
    <h1>LegalBro</h1> 
    <div class="form-container">
        <form action="/ask" enctype="multipart/form-data" method="post">
            <input name="query" type="text" placeholder="Enter your query, doubt or situation">
            <input type="submit" value="Ask">
        </form>
    </div>
    <p>*elaborate your situation for us to help you better</p>
</body>
</html>
"""

