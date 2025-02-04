# car_managements

### Running the application:
python car.py 

### Testing the endpoints:
http://127.0.0.1:5000/cars
returns:
[
    {
        "id": 1,
        "make": "Toyota",
        "model": "Corolla",
        "price": 25000,
        "year": 2022
    },
    {
        "id": 2,
        "make": "Honda",
        "model": "Civic",
        "price": 27000,
        "year": 2023
    },
    {
        "id": 3,
        "make": "Ford",
        "model": "Mustang",
        "price": 40000,
        "year": 2021
    },
    {
        "id": 4,
        "make": "BMW",
        "model": "X5",
        "price": 60000,
        "year": 2023
    },
    {
        "id": 5,
        "make": "Mercedes",
        "model": "C-Class",
        "price": 55000,
        "year": 2022
    },
    {
        "id": 6,
        "make": "Audi",
        "model": "A4",
        "price": 42000,
        "year": 2023
    },
    {
        "id": 7,
        "make": "Nissan",
        "model": "Altima",
        "price": 28000,
        "year": 2021
    }
]

http://127.0.0.1:5000/cars/5
returns:
{
    "id": 5,
    "make": "Mercedes",
    "model": "C-Class",
    "price": 55000,
    "year": 2022
}

http://127.0.0.1:5000/addcars
returns:
{
    "id": 8,
    "make": "Ford",
    "model": "Mustang",
    "price": 55000,
    "year": 2024
}

http://127.0.0.1:5000/updatecars/1
returns:
{
    "id": 1,
    "make": "Toyota",
    "model": "Camry",
    "price": 30000,
    "year": 2025
}
http://127.0.0.1:5000/deletecars/2
returns:
{
    "message": "Car deleted"
}

http://127.0.0.1:5000/manufacturers
returns:
[
    {
        "id": 1,
        "name": "Toyota"
    },
    {
        "id": 2,
        "name": "Honda"
    },
    {
        "id": 3,
        "name": "Ford"
    },
    {
        "id": 4,
        "name": "BMW"
    },
    {
        "id": 5,
        "name": "Mercedes"
    },
    {
        "id": 6,
        "name": "Audi"
    },
    {
        "id": 7,
        "name": "Nissan"
    }
]

http://127.0.0.1:5000/addmanufacturer
returns:
{
    "country": "USA",
    "id": 8,
    "name": "Buggati"
}

http://127.0.0.1:5000/models/2
returns:
[
    {
        "id": 2,
        "manufacturer_id": 2,
        "name": "Civic"
    }
]

http://127.0.0.1:5000/customers
return:
[
    {
        "email": "joel@gmail.com",
        "id": 1,
        "name": "Joel Kurivilla"
    },
    {
        "email": "allen@gmail.com",
        "id": 2,
        "name": "Allen Shibu"
    },
    {
        "email": "mathew@gmail.com",
        "id": 3,
        "name": "Mathews Mathew"
    },
    {
        "email": "rosh@gmail.com",
        "id": 4,
        "name": "Rosh R"
    },
    {
        "email": "anish@gmail.com",
        "id": 5,
        "name": "Anish Pillai"
    },
    {
        "email": "chacko@gmail.com",
        "id": 6,
        "name": "Ryan Chacko"
    },
    {
        "email": "khan@gmail.com",
        "id": 7,
        "name": "Danish Khan"
    }
]

http://127.0.0.1:5000/customers/4
returns:
{
    "email": "rosh@gmail.com",
    "id": 4,
    "name": "Rosh R"
}







