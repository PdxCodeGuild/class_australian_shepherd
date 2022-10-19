// Overview -----------------------------------------------------

// Objects are composed of primitive types. 

let contact = {
    firstName: 'Jane',
    lastName: 'Doe',
    age: 34
}

// console.log(contact.firstName) // Jane


// Objects as Dictionaries


// Objects can be used like dictionaries, with keys instead of properties. 
// This can allow you to use letters in keys that wouldn't ordinarily be possible, 
// like leading numbers and hyphens.

let contact_2 = {
    'name': 'Jane',
    0: 'use a number as a key',
    'third-key': 'or use a hyphen'
}

console.log(contact_2['name']) // Jane
console.log(contact_2[0]) // 0 
console.log(contact_2['third-key']) // or use a hyphen

// Navigating Data ---------------------------------------------------------------------------------------------

let library_user = {
    first_name: 'Jane',
    last_name: 'Smith',
    age: 20,
    books: [
        {
            title: 'A Wrinkle in Time',
            author: "Madeline L\'Engle",
            published: 192
        },
        {
            title: 'The Giving Tree',
            author: 'Shel Silverstein',
            published: 1964
        }
    ]

}


console.log(library_user.first_name) // Jame

console.log(library_user.books[0].title) // A Wrinkle in Time