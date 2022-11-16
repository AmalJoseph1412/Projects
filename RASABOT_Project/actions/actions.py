# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
import re

class ValidateMobNoForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_mob_no_form"

    def validate_mobno(
        self,
        slot_value:Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text,Any]:
        """Validate mobile number value."""
        extract_phone_number_pattern = "^\\+?[0-9][0-9]{7,12}$"
        if re.findall(extract_phone_number_pattern, Dict):
            # validation succeeded, set the value of the "mob_no" slot to value
            return {"mob_no": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            dispatcher.utter_message(text="Enter a valid mobile number.")
            return {"mob_no": None}

class checkUser(Action):
    def name(self) -> Text:
        return "checkUser"

    def chk_user(
        self,
        slot_value:Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text,Any]]:
        mob_no_slot_value= tracker.get_slot('mob_name')

        """Query for fetching list of mobile numbers instead using a list, list_mob"""

        list_mob= ["9898989898","7878787878","6565656565","4747474747","9447131761"]
        for i in list_mob:
            if i==mob_no_slot_value:
            # if user exists, set the value of the "user_chk" slot to true
                SlotSet("user_chk", "true")
        else:
            # new user
            SlotSet("user_chk", "false")

        
    class getSlots(Action):
        def name(self) -> Text:
            return "getSlots"

        def get_slots(
        self,
        slot_value:Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text,Any]]:
    
            user_info_txt= tracker.get_slot('user_info')
            user_info_list= user_info_txt.split("-")
            name=user_info_list[0]
            age=user_info_list[1]
            gender=user_info_list[2]
        """Query for writing the slot values to """

    
