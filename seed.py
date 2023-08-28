from posts.models import Post
from django.conf import settings
import json
# import os

# os.environ['DJANGO_SETTINGS_MODULE'] = 'pet_pals.settings'


# pets_json = """[
#     {
#         "Name": "Ruby",
#         "Age": 2,
#         "AnimalType": "Dog",
#         "Breed": "Australian Shepherd",
#         "Description": "Ruby is a lively and intelligent Australian Shepherd with a striking merle coat. She loves playing fetch and going on long hikes.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Leo",
#         "Age": 3,
#         "AnimalType": "Cat",
#         "Breed": "Russian Blue",
#         "Description": "Leo is a sophisticated Russian Blue cat with gorgeous silver-blue fur. He enjoys lounging in sunlit spots and engaging in thoughtful conversations with his human companions.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Cooper",
#         "Age": 1,
#         "AnimalType": "Dog",
#         "Breed": "Corgi",
#         "Description": "Meet Cooper, a playful and adorable Corgi puppy. With his short legs and big personality, he's always the center of attention wherever he goes.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Mila",
#         "Age": 2,
#         "AnimalType": "Cat",
#         "Breed": "Himalayan",
#         "Description": "Mila is a stunning Himalayan cat with a luxurious long coat and striking blue eyes. Her calm demeanor and affectionate nature make her the perfect lap cat.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Jackson",
#         "Age": 4,
#         "AnimalType": "Dog",
#         "Breed": "Bulldog",
#         "Description": "Jackson is a gentle Bulldog with a heart of gold. Despite his tough appearance, he's a true softie who adores belly rubs and snuggling on the couch.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Chloe",
#         "Age": 1,
#         "AnimalType": "Cat",
#         "Breed": "Birman",
#         "Description": "Chloe is a playful and mischievous Birman kitten with striking blue eyes. She loves chasing feather toys and exploring every nook and cranny of her surroundings.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Maximus",
#         "Age": 5,
#         "AnimalType": "Dog",
#         "Breed": "Rottweiler",
#         "Description": "Maximus is a loyal and protective Rottweiler with a heart of gold. He's excellent with kids and is always ready to play a game of tug-of-war.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Lily",
#         "Age": 2,
#         "AnimalType": "Cat",
#         "Breed": "Exotic Shorthair",
#         "Description": "Lily is an Exotic Shorthair cat with a sweet and easygoing personality. Her plush coat and round face make her irresistibly cute and huggable.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Duke",
#         "Age": 3,
#         "AnimalType": "Dog",
#         "Breed": "Great Dane",
#         "Description": "Duke is a majestic Great Dane with a gentle disposition. Despite his massive size, he thinks he's a lap dog and loves curling up beside his family.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Mochi",
#         "Age": 1,
#         "AnimalType": "Cat",
#         "Breed": "Japanese Bobtail",
#         "Description": "Mochi is a curious and energetic Japanese Bobtail kitten. Her short, bobbed tail and playful antics are bound to bring smiles to your face.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Bailey",
#         "Age": 6,
#         "AnimalType": "Dog",
#         "Breed": "Shetland Sheepdog",
#         "Description": "Bailey is a loyal and intelligent Shetland Sheepdog with a beautiful sable coat. She excels in agility training and loves learning new tricks.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Felix",
#         "Age": 2,
#         "AnimalType": "Cat",
#         "Breed": "Manx",
#         "Description": "Felix is a playful and tailless Manx cat with a boundless curiosity. He's always on the lookout for new adventures and interesting things to pounce on.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Sadie",
#         "Age": 4,
#         "AnimalType": "Dog",
#         "Breed": "Siberian Husky",
#         "Description": "Sadie is an energetic and independent Siberian Husky with striking blue eyes. She loves outdoor activities and thrives in colder climates.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Ollie",
#         "Age": 1,
#         "AnimalType": "Cat",
#         "Breed": "Sphynx",
#         "Description": "Ollie is a unique and affectionate Sphynx cat. Despite his lack of fur, he's always warm-hearted and loves cuddling up with his human companions.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Rosie",
#         "Age": 5,
#         "AnimalType": "Dog",
#         "Breed": "Pug",
#         "Description": "Rosie is a charming Pug with a delightful personality. Her wrinkled face and curly tail are matched only by her love for belly rubs and treats.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Sam",
#         "Age": 3,
#         "AnimalType": "Cat",
#         "Breed": "American Shorthair",
#         "Description": "Sam is a friendly and easygoing American Shorthair cat. He gets along with everyone, both humans and other pets, and enjoys lounging around the house.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Maggie",
#         "Age": 2,
#         "AnimalType": "Dog",
#         "Breed": "Cocker Spaniel",
#         "Description": "Maggie is a joyful and affectionate Cocker Spaniel. Her expressive eyes and wagging tail are sure to brighten even the gloomiest days.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Toby",
#         "Age": 1,
#         "AnimalType": "Cat",
#         "Breed": "Turkish Van",
#         "Description": "Toby is an adventurous and playful Turkish Van kitten. With his love for water and mischievous spirit, he's a constant source of entertainment.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Sophie",
#         "Age": 4,
#         "AnimalType": "Dog",
#         "Breed": "Golden Retriever",
#         "Description": "Sophie is a gentle and affectionate Golden Retriever with a heart of gold. Her love for people and her friendly nature make her an ideal family pet.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Charlie",
#         "Age": 2,
#         "AnimalType": "Cat",
#         "Breed": "Scottish Fold",
#         "Description": "Charlie is a Scottish Fold cat with a distinctive folded ear that adds to his charm. He's a laid-back and easy-to-please feline companion.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Lola",
#         "Age": 5,
#         "AnimalType": "Dog",
#         "Breed": "Dachshund",
#         "Description": "Lola is a spunky and lively Dachshund with a big personality. Her short legs don't stop her from exploring and keeping up with her human friends.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Leo",
#         "Age": 3,
#         "AnimalType": "Cat",
#         "Breed": "Maine Coon",
#         "Description": "Leo is a majestic Maine Coon cat with a thick and luxurious coat. Despite his large size, he's a gentle giant who loves to cuddle.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Bella",
#         "Age": 1,
#         "AnimalType": "Dog",
#         "Breed": "French Bulldog",
#         "Description": "Bella is an adorable French Bulldog with expressive ears and a loving personality. She's happiest when she's in the company of her favorite humans.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Milo",
#         "Age": 2,
#         "AnimalType": "Cat",
#         "Breed": "Siamese",
#         "Description": "Milo is a Siamese cat with striking blue eyes and a vocal personality. He's always ready to engage in conversations and share his thoughts.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Bailey",
#         "Age": 4,
#         "AnimalType": "Dog",
#         "Breed": "Australian Cattle Dog",
#         "Description": "Bailey is an intelligent and energetic Australian Cattle Dog. With her boundless energy and agility, she's a great partner for outdoor activities.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Oliver",
#         "Age": 1,
#         "AnimalType": "Cat",
#         "Breed": "Ragdoll",
#         "Description": "Oliver is a Ragdoll cat with soulful blue eyes and a gentle temperament. He enjoys lounging in his human's lap and getting chin scratches.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Rocky",
#         "Age": 5,
#         "AnimalType": "Dog",
#         "Breed": "Boxer",
#         "Description": "Rocky is a fun-loving and enthusiastic Boxer. His boundless energy and signature \"wiggle butt\" make him a favorite among his human friends.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Luna",
#         "Age": 2,
#         "AnimalType": "Cat",
#         "Breed": "Persian",
#         "Description": "Luna is a regal Persian cat with a luxurious coat that requires extra care. She's a quiet and elegant presence in any room she enters.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Bentley",
#         "Age": 3,
#         "AnimalType": "Dog",
#         "Breed": "Poodle",
#         "Description": "Bentley is an elegant and intelligent Poodle. With his hypoallergenic coat and friendly demeanor, he's a wonderful companion for those with allergies.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Zoe",
#         "Age": 1,
#         "AnimalType": "Cat",
#         "Breed": "British Shorthair",
#         "Description": "Zoe is a British Shorthair cat with a plush and dense coat. Her round face and calm disposition make her a picture-perfect lap companion.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Charlie",
#         "Age": 4,
#         "AnimalType": "Dog",
#         "Breed": "Labrador Retriever",
#         "Description": "Charlie is a Labrador Retriever known for his boundless enthusiasm and friendly nature. He's always up for a game of fetch or a swim in the lake.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Mia",
#         "Age": 2,
#         "AnimalType": "Cat",
#         "Breed": "Scottish Fold",
#         "Description": "Mia is a Scottish Fold cat with a playful and affectionate personality. Her folded ears and charming antics make her a favorite among cat lovers.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Oscar",
#         "Age": 5,
#         "AnimalType": "Dog",
#         "Breed": "Beagle",
#         "Description": "Oscar is a cheerful and curious Beagle with a keen sense of smell. He's always on the hunt for new scents and exciting adventures.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Lily",
#         "Age": 1,
#         "AnimalType": "Cat",
#         "Breed": "Siberian",
#         "Description": "Lily is a Siberian cat with a thick triple coat that's perfect for colder climates. Her playful nature and affectionate demeanor warm the hearts of all who meet her.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Tucker",
#         "Age": 6,
#         "AnimalType": "Dog",
#         "Breed": "Border Collie",
#         "Description": "Tucker is a highly intelligent and energetic Border Collie. He excels in dog sports and is always eager to learn new tricks and commands.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Lucy",
#         "Age": 3,
#         "AnimalType": "Cat",
#         "Breed": "Ragdoll",
#         "Description": "Lucy is a Ragdoll cat with stunning blue eyes and a gentle disposition. She's happiest when she's curled up on a soft blanket, enjoying a nap.",
#         "Gender": "Female"
#     },
#     {
#         "Name": "Teddy",
#         "Age": 4,
#         "AnimalType": "Dog",
#         "Breed": "Cavalier King Charles Spaniel",
#         "Description": "Teddy is a lovable and affectionate Cavalier King Charles Spaniel. His large, expressive eyes and wagging tail make him impossible to resist.",
#         "Gender": "Male"
#     },
#     {
#         "Name": "Chloe",
#         "Age": 2,
#         "AnimalType": "Cat",
#         "Breed": "Bengal",
#         "Description": "Chloe is a Bengal cat with striking leopard-like spots and a playful personality. She's always ready to pounce and explore her surroundings.",
#         "Gender": "Female"
#     }
# ]"""

with open('data.json') as f:
    data = json.load(f)


settings.configure()

for data in data:
    Post(
        name=data['Name'],
        age=data['Age'],
        animal_type=data['AnimalType'],
        breed=data['breed'],
        description=data['Description'],
        gender=data['Gender']
    ).save()
