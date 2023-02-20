class GQLEnum:
    '''
    Wrapper class/type for GraphQL enums whose value needs to be injected
    directly into queries instead of being wrapped as a string
    '''

    def __init__(self, name) -> None:
        self.enum_name = name

    def __repr__(self) -> str:
        return self.enum_name
