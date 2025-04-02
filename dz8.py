<head>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>


body {
    font-family: Arial, sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 20px auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333;
    text-align: center;
}

button {
    background: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #0056b3;
}



<div class="container">
    <h1>📋 Список задач</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task.name }} <button>Удалить</button></li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_task') }}"><button>Добавить задачу</button></a>
</div>
