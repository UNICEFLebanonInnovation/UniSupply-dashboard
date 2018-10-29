# UniSupply Dashboard
Healthy Camp Monitoring Tool for hygiene monitoring using Power Bi and Kobo

### Prerequisites

A python environment on any platform with MongoDB installed

### Installing

Install requirements

```
$ pip install -r requirements.txt
```

## Importing Data

```
$ export FLASK_APP=tasks.py
$ import_form_data KOBO_ID KOBO_USERNAME KOBO_PASSWORD
Run on terminal: mongod
Run on another terminal:
export FLASK_APP=tasks.py
python -m flask run
flask import_form_data 108163 unicef_leb PRIME2017
flask convert_to_integer
flask run_aggregation

https://docs.mongodb.com/manual/reference/operator/aggregation/add/
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](http://flask.pocoo.org) - The web framework used

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Ali Chamseddine** - *First Version* - [achamseddine](https://github.com/achamseddine)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc


