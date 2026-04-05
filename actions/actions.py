from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProvideSymptomGuidance(Action):

    def name(self) -> Text:
        return "action_provide_symptom_guidance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get extracted entity
        symptom = next(tracker.get_latest_entity_values("symptom"), None)

        if symptom == "fever":
            dispatcher.utter_message(
                text="For fever, rest, stay hydrated, and monitor your temperature. Seek medical care if it becomes severe."
            )

        elif symptom == "headache":
            dispatcher.utter_message(
                text="For headaches, rest, hydrate, and reduce stress. If severe or persistent, consult a healthcare professional."
            )

        elif symptom == "chills":
            dispatcher.utter_message(
                text="Chills may be a sign of infection. Monitor your condition and seek medical care if symptoms worsen."
            )

        else:
            dispatcher.utter_message(
                text="I understand your symptoms. Please monitor your health and consult a medical professional if necessary."
            )

        return []