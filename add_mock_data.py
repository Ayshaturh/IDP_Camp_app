import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'idp.settings')
django.setup()

from base.models import Child

# Mock data for children with longer descriptions
children_data = [
    {
        "name": "Amina Yusuf",
        "age": 7,
        "description": "Amina is a bright and cheerful girl who loves drawing and reading stories. She enjoys spending her afternoons sketching nature scenes and often dreams of becoming an artist. Her favorite books are filled with fairy tales and adventure stories, which she loves to read aloud to her friends.",
        "gender": "Female",
        "image": "static/children_photos/amina_sani.jpg"
    },
    {
        "name": "Hassan Abubakar",
        "age": 6,
        "description": "Hassan enjoys playing football and has a keen interest in science. His curiosity about how things work keeps him busy experimenting with small science projects. He is always eager to learn new things and share his discoveries with his classmates. Football is his passion, and he dreams of playing professionally one day.",
        "gender": "Male",
        "image": "static/children_photos/hassan_abubakar.jpg"
    },
    {
        "name": "Fatima Usman",
        "age": 8,
        "description": "Fatima is a talented singer with a love for music and dancing. She is often found humming her favorite tunes and choreographing dance routines with her friends. Fatima’s voice has a magical quality that captivates everyone who hears her sing. She hopes to one day perform on a big stage and share her music with the world.",
        "gender": "Female",
        "image": "static/children_photos/fatima_usman.jpg"
    },
    {
        "name": "Aliyu Bello",
        "age": 10,
        "description": "Aliyu is an avid reader and enjoys solving puzzles and riddles. His love for books is matched only by his talent for uncovering the solutions to complex problems. Aliyu spends hours at the library, exploring different genres and expanding his knowledge. His analytical mind and sharp wit make him a natural problem solver, and he dreams of becoming an engineer.",
        "gender": "Male",
        "image": "static/children_photos/aliyu_bello.jpg"
    },
    {
        "name": "Maryam Sani",
        "age": 6,
        "description": "Maryam is a shy but very intelligent girl who loves playing with dolls. Despite her quiet nature, she is incredibly perceptive and often surprises others with her insightful observations. Maryam’s creativity shines through in the elaborate stories she creates for her dolls. She dreams of becoming a writer and hopes to publish her own books one day.",
        "gender": "Female",
        "image": "static/children_photos/maryam_sani.jpg"
    }
]

# Adding mock data to the database
for child in children_data:
    Child.objects.create(
        name=child["name"],
        age=child["age"],
        description=child["description"],
        gender=child["gender"],
        image=child["image"]
    )
