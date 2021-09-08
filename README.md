# testproject

## Requirement
Python=3.9

Django=3.x

## HOW TO SETUP:
- install requirements
`pip install -r requirements.txt`
- Run migrations `python manage.py migrate`
- Create superuser `python manage.py createsuperuser`
- Run the project  `python manage.py runserver`




###QUERY AND MUTATIONS:
````
query  {
  allBusiness (name_Icontains: "test"){
    edges {
      node {
        id,
        name,
        employeeSize,
        address,
        owner {
          id,
          username,
          password,
          firstName,
          lastName
        }
      }
    }
  }
}

query {
  allUsers {
    edges {
      node {
        id,
        username
      }
    }
  }
}


mutation myFirstMutation {
  createBusiness(businessData: {name:"Busines111", address:"test add", employeeSize: 20, owner:"VXNlclR5cGU6MQ=="}) {
    business {
      name,
      id
    }	
  }
}

mutation myFirstMutation {
  updateBusiness(name:"Busines23", id:"QnVzaW5lc3Nlc1R5cGU6Ng==") {
    business {
      name
    }	
  }
}


mutation myFirstMutation {
  deleteBusiness( id:"QnVzaW5lc3Nlc1R5cGU6Ng==") {
    business {
      name
    }	
  }
}

