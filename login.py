from mailchimp3 import MailChimp
import os
import pprint
import time
import json

# Login to MailChimp Client with API key and username
client = MailChimp(mc_api=os.environ['MAILCHIMP_API_KEY'], mc_user=os.environ['BUSN_EMAIL'])

# Current campaigns
# myCampaigns = client.campaigns.all(get_all=True)
# print(myCampaigns)

# Received all current lists (audience) information. Need the ID
myLists = client.lists.all(get_all=False)
# print(myLists)

# Need list id to make a campaign. id comes from MyLists nested dict
mc_list_id = myLists['lists'][0]['id']
# print(mc_list_id)


"""Creates a new campaign"""

# # Required information for data argument. testing with plaintext
# data_dict = {
#         "recipients":
#         {
#             "list_id": mc_list_id
#         },
#         "settings":
#         {
#             "subject_line": 'test',
#             "from_name": 'Yusuf',
#             "reply_to": os.environ['BUSN_EMAIL']
#         },
#         "type": "plaintext"
#     }

# Saving instance of new campaign in a variable

"""
input
    list ID that connects to audience(?)
output
    creates a new campaign. invoking will provide an Campaign ID for
    reference
"""
# new_campaign = client.campaigns.create(data = data_dict)



"""Update content into new campaign"""
# mc_camp_id = "7dc8db005a"
# # mc_camp_id = 309745
# camp = client.campaigns.get(campaign_id=mc_camp_id)


# TODO: The instance isn't updating. might have to sleep between the creation
# the update?

# Updating content
# client.campaigns.content.update(campaign_id=mc_camp_id,
#             data={"message":"Checking to see is this works"})

# res = client.campaigns.content.get(campaign_id=mc_camp_id)
# print(res)


r = client.campaigns.content.get(campaign_id='c2df2c2e25')
print(r)
