#region Imports
from abc import abstractclassmethod, abstractproperty;
#endregion Imports

class ResponseBase:    
    def __init__(cls, rawResponse:str):
        cls._rawResponse = rawResponse;

    @abstractclassmethod
    def ParseResponse(cls):
        pass;
    
    @abstractproperty
    def RawResponse(cls):
        '''Raw JSON response from OddsJam API'''
        return cls._rawResponse;
    
    @RawResponse.setter
    def RawResponse(cls, newRawResponse):
        cls._rawResponse = newRawResponse