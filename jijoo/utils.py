from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

NG_MOBILE_PREFIXES = {
    "mtn": [
        "0803",
        "0703",
        "0903",
        "0806",
        "0706",
        "0813",
        "0814",
        "0816",
        "0810",
        "0906",
        "07025",
        "07026",
        "0704",
    ],
    "glo": ["0805", "0705", "0905", "0807", "0815", "0905", "0811"],
    "airtel": ["0802", "0902", "0701", "0808", "0708", "0812", "0901", "0907"],
    "9mobile": ["0809", "0909", "0817", "0818", "0908"],
    "ntel": ["0804"],
    "smile": ["0702"],
    "multilinks": ["0709", "07027"],
    "visafone": ["07025", "07026", "0704"],
    "starcomms": ["07028", "07029", "0819"],
    "zoom": ["0707"],
}

STATES = [
  "Abia",
  "Adamawa",
  "Akwa Ibom",
  "Anambra",
  "Bauchi",
  "Bayelsa",
  "Benue",
  "Borno",
  "Cross River",
  "Delta",
  "Ebonyi",
  "Edo",
  "Ekiti",
  "Enugu",
  "FCT - Abuja",
  "Gombe",
  "Imo",
  "Jigawa",
  "Kaduna",
  "Kano",
  "Katsina",
  "Kebbi",
  "Kogi",
  "Kwara",
  "Lagos",
  "Nasarawa",
  "Niger",
  "Ogun",
  "Ondo",
  "Osun",
  "Oyo",
  "Plateau",
  "Rivers",
  "Sokoto",
  "Taraba",
  "Yobe",
  "Zamfara"
]


def validate_ng_mobile_number(mobile_number):
    try:
        int(mobile_number)
    except ValueError:
        raise ValidationError(_("Enter a valid Nigerian mobile number"), code=400)
    if len(mobile_number) != 11:
        raise ValidationError("Enter 11 digit mobile number", code=400)
    # check if it starts with any prefix [0807,0906 etc..]
    if mobile_number[:1] != "0" and (
        (
            mobile_number[:5] in NG_MOBILE_PREFIXES
            or mobile_number[:4] in NG_MOBILE_PREFIXES
        )
    ):
        raise ValidationError(_("Enter a valid Nigerian mobile number"))


def validate_state(state):

    if state and str(state).capitalize() not in STATES:
        raise ValidationError(_("Invalid Nigerian state"))
