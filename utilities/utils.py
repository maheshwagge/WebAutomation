class Utils:

    def assert_list_item_text(self, list_web_element, value):
        for stop in list_web_element:
            print("The Text is: ", + stop.text)
            assert stop.text == value
            print("assert pass")


