
class VerifyDataUtils:
    userEnpoint = ['emai', 'first_name', 'last_name', 'phone']
    def endpoint(self, endpoint):
        if endpoint == 'userEendpoint':
            return self.userEnpoint

    def verifyEmptyData(self, target, endpoint):
        reference = self.endpoint(endpoint)

        for k in reference:
            if k not in target:
                return False
            elif target[k] == '' or target[k] == None:
                return False

        return True
