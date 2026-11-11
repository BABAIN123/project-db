from models import Post, User, engine
from sqlalchemy.orm import sessionmaker

# Создаем сессию для работы с базой
Session = sessionmaker(bind=engine)
session = Session()

print("Добавляем тестовых пользователей...")
users = [
    User(name=f"User {i}", email=f"user{i}@example.com") for i in range(1, 6)
]
session.add_all(users)
session.commit()  # Сохраняем пользователей, чтобы у них появились ID

print("Добавляем тестовые посты (10+ штук)...")
posts = [
    Post(
        title=f"Post title {i}",
        content=f"Content for post number {i}",
        user_id=(i % 5) + 1,
    )
    for i in range(1, 12)
]

session.add_all(posts)
session.commit()  # Сохраняем посты

print("База данных успешно заполнена тестовыми данными!")
session.close()