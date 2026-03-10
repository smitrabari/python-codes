# Dictionaries
# Stored in sets{}
capitals = {"usa":"Washington D.C.",
            "india":"Delhi",
            "japan":"Tokiyo"}
print(dir(capitals)) # For all Dictionaries
print(help(capitals)) # For all Dictionaries info.
print(capitals.get("india")) # to find Dictionaries from elements.
print(capitals.get("russia")) # if no element is present then it will show NONE.
capitals.update({"germany":"berlin"}) # to add elements.