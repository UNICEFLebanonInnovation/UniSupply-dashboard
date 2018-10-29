import json
import bson
import click
from os import path

import requests
from requests.auth import HTTPBasicAuth

from app import app, db


def _get_aggreagation(name):
    with open('distributions.json') as json_data:
        return json.load(json_data)


@click.argument('password')
@click.argument('username')
@app.cli.command()
def import_form_data(
        url='http://unisyncgtwy.westeurope.cloudapp.azure.com:4984/leb-winter-prd',
        username='',
        password='',
        collection='winter_submissions'
):
    """Initialize the database."""
    click.echo('Staring import from Kobo...')

    url = path.join(url, '_all_docs?include_docs=true')
    print(url)

    data = requests.get(
        url,
        auth=HTTPBasicAuth(username, password)
    ).json()

    data = data['rows']

    db.connection.get_default_database()[collection].drop()
    db.connection.get_default_database()[collection].insert_many(data)
    # db.connection.get_default_database()[collection].insert_one(data)
    click.echo('{} submissions imported from Kobo'.format(len(data)))


# @app.cli.command()
# def convert_to_integer(
#         collection='submissions',
#         field_name='Metadata_section/site_data/sample_tents'
# ):
#     for form in db.connection.get_default_database()[collection].find():
#         if field_name not in form:
#             continue
#         form[field_name] = int(form[field_name])
#         db.connection.get_default_database()[collection].save(form)


@app.cli.command()
def run_aggregation(
        collection='winter_submissions',
        file_name='distributions'
):
    click.echo(db.connection.get_default_database().command(
        'aggregate',
        collection,
        pipeline=_get_aggreagation(file_name),
        allowDiskUse=True,
        cursor={},
        # explain=True
    ))
