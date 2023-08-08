 def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """returns the decoded value of a base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            value = base64.b64decode(base64_authorization_header)
            return value.decode('utf-8')
        except ValueError:
            return None
