# This is an automatically generated file.

from __future__ import print_function # For Python 2.7+ Compatibility
import contentful

# Define your Credentials

SPACE_ID = 'cfexampleapi'
ACCESS_TOKEN = 'b4c0n73n7fu1'

# Create your Contentful Delivery API Client

client = contentful.Client(SPACE_ID, ACCESS_TOKEN)

# Fetch all your entries

entries = client.entries()

# Print all the entry IDs

print("Here's the list of your first 100 entries:")
for entry in entries:
    print("\t{0}".format(entry.id))

# Feel free to customize this snippet as much as you like.
# To learn more, check out our Python Tutorials and Integrations: https://www.contentful.com/developers/docs/python/
