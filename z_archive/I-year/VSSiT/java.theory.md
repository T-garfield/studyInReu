# JAVA

## **General_Commands:**
- Random #
```js
- Math.floor(Math.random() * 100)
```

- Khai bao VAR:
```js
var
let
const
```

- Khai bao Function:
```js
let remotelyDisable = obj => {
  obj.disabled = true;
}
```

## **Function**

**- Arrows:**
```js
const goat = {
  dietType: 'herbivore',
  makeSound() {
    console.log('baaa');
  },
  diet: () => {
    console.log(this.dietType);
  }
};
```
**- Long:**
```js
const goat = {
  name: 'Billy',
  color: 'biege',
  giveDetails: function() {
    console.log(`${this.name} is a ${this.color} goat.`)
  }
}
```
**- Short:**
```js
const goat = {
  name: 'Billy',
  color: 'biege',
  giveDetails(){
    console.log(`${this.name} is a ${this.color} goat.`)
  }
}
```

## **Arrays**
- Khai bao Array:

```js
let <ten.array> = ['elements', 'elements', ...];

const <ten.array> = [[], [],... ]; //nested array
```

- Others:
```js
    1. <ten.array>[index#]
    2. console.log(`<ten.array>`.length)
    3. <ten.array>.push('elements1, elements2, ...')
	4. <ten.array>.pop //remove the last item
```

### .method commands
- .indexOf
- .shift
- .unshift
- .slice

## **LOOPS**
```js
// Write your code below
for (let counter = 5; counter <11; counter++)
{
  console.log(counter)
}

// Loop bwards
for (let counter = 3; counter >= 0; counter--){
  console.log(counter);
}

// For ...?
for (let i = 0; i < vacationSpots.length; i++){
  console.log('I would love to visit '+vacationSpots[i])

//nested.loops
const bobsFollowers = ['a','b','c','d']
const tinasFollowers = ['a','b','e']
let mutualFollowers = []
for (let i = 0; i < bobsFollowers.length; i++) {
  for (let j = 0; j < tinasFollowers.length; j++) {
    if (bobsFollowers[i] === tinasFollowers[j]) {
      mutualFollowers.push(bobsFollowers[i])
    }
  }
};

//while loop
while ( currentCard != 'spade') {
  currentCard = cards[Math.floor(Math.random() * 4)];
	console.log(currentCard);
}
```

## **Objects**
```js
let spaceship = {}; // spaceship is an empty object
```

*We make a key-value pair by writing the key’s name, or identifier, followed by a colon and then the value. We separate each key-value pair in an object literal with a comma* `(,)`. *Keys are strings, but when we have a key that does not have any special characters in it, JavaScript allows us to omit the quotation marks.*

```js
let spaceship = {
  homePlanet: 'Earth',
  color: 'silver'
};
spaceship.homePlanet; // Returns 'Earth',
spaceship.color; // Returns 'silver',

let spaceship = {
  'Fuel Type': 'Turbo Fuel',
  'Active Duty': true,
  homePlanet: 'Earth',
  numCrew: 5
};
spaceship['Active Duty'];   // Returns true
spaceship['Fuel Type'];   // Returns  'Turbo Fuel'
spaceship['numCrew'];   // Returns 5
spaceship['!!!!!!!!!!!!!!!'];   // Returns undefined

let returnAnyProp = (objectName, propName) => objectName[propName];

returnAnyProp(spaceship, 'homePlanet'); // Returns 'Earth'
```

### - Property Assignment:
```js
const spaceship = {type: 'shuttle'};
spaceship = {type: 'alien'}; // TypeError: Assignment to constant variable.
spaceship.type = 'alien'; // Changes the value of the type property
spaceship.speed = 'Mach 5'; // Creates a new key of 'speed' with a value of 'Mach 5'

delete spaceship.mission;  // Removes the mission property

```

### - Methods:

*When the data stored on an object is a function we call that a method. A property is what an object has, while a method is what an object does*

*Do object methods seem familiar? That’s because you’ve been using them all along! For example console is a global javascript object and .log() is a method on that object. Math is also a global javascript object and .floor() is a method on it.*

```js
const alienShip = {
  retreat () {
    console.log(retreatMessage);
  }, //dont forget commas
  takeOff () {
    console.log('Spim... Borp... Glix... Blastoff!');
  }
}
```
- Calling method:

```js
alienShip.retreat()
alienShip.takeOff()
```

### - Looping Through Objects
*Loops are programming tools that repeat a block of code until a condition is met. We learned how to iterate through arrays using their numerical indexing, but the key-value pairs in objects aren’t ordered!* [*JavaScript has given us alternative solution for iterating through objects with the* `for...in` *syntax*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in).

```js
let spaceship = {
    crew: {
    captain: { 
        name: 'Lily', 
        degree: 'Computer Engineering', 
        cheerTeam() { console.log('You got this!') } 
        },
    'chief officer': { 
        name: 'Dan', 
        degree: 'Aerospace Engineering', 
        agree() { console.log('I agree, captain!') } 
        },
    medic: { 
        name: 'Clementine', 
        degree: 'Physics', 
        announce() { console.log(`Jets on!`) } },
    translator: {
        name: 'Shauna', 
        degree: 'Conservation Science', 
        powerFuel() { console.log('The tank is full!') } 
        }
    }
}; 

// Write your code below
for (let a in spaceship.crew) {
  console.log(`${a}: ${spaceship.crew[a].name}`)
}

for (let a in spaceship.crew) {
  console.log(`${spaceship.crew[a].name}: ${spaceship.crew[a].degree}`)
}
```

## **Advanced Objects**

### - `This` keyword

```js
const robot = {
  model: '1E78V2',
  energyLevel: 100,
  provideInfo() {
    return 'I am ' + this.model + ' and my current energy level is ' + this.energyLevel
  }
};

console.log(robot.provideInfo())
```

### - Privacy

*One common convention is to place an underscore `_` before the name of a property to mean that the property should not be altered. Here’s an example of using `_` to prepend a property.*
```js
const bankAccount = {
  _amount: 1000
}
```
*Even so, it is still possible to reassign* `_amount`:
```js
bankAccount._amount = 1000000;
```

### - Getters


```
const robot = {
  _model: '1E78V2',
  _energyLevel: 100,
  get energyLevel(){
    if(typeof this._energyLevel === 'number') {
      return 'My current energy level is ' + this._energyLevel
    } else {
      return "System malfunction: cannot retrieve energy level"
    }
  }
};

console.log(robot.energyLevel);
```

### - Setters

Now that we’ve gone over syntax, let’s discuss some notable advantages of using getter methods:
* *Getters can perform an action on the data when getting a property.*
* *Getters can return different values using conditionals.*
* *In a getter, we can access the properties of the calling object using this.*
* *The functionality of our code is easier for other developers to understand.*
  
*Another thing to keep in mind when using getter (and setter) methods is that properties cannot share the same name as the getter/setter function. If we do so, then calling the method will result in an infinite call stack error. One workaround is to add an underscore before the property name like we did in the example above.*

```js
const robot = {
  _model: '1E78V2',
  _energyLevel: 100,
  _numOfSensors: 15,
  get numOfSensors(){
    if(typeof this._numOfSensors === 'number'){
      return this._numOfSensors;
    } else {
      return 'Sensors are currently down.'
    }
  },
  set numOfSensors(num) {
    if (typeof num === 'number' && num >= 0) {
      this._numOfSensors = num;
    } else {
      console.log('Pass in a number that is greater than or equal to 0');
    }
  }
};


robot.numOfSensors = 100
console.log(robot.numOfSensors)
```

