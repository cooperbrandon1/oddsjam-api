#region Imports
from abc import abstractclassmethod, abstractproperty
import pandas as pd
import json;
#endregion Imports
class ResponseBase:    
    def __init__(cls, rawResponse:str):
        cls._rawResponse = rawResponse;

    @classmethod
    def ToDataFrame(cls,obj, idx):
        df = pd.DataFrame(obj);
        df.set_index(idx);
        return df;

    @abstractclassmethod
    def ParseResponse(cls, rawResponse:str):
        pass;
    
    @abstractproperty
    def RawResponse(cls):
        '''Raw JSON response from OddsJam API'''
        return cls._rawResponse;
    
    @RawResponse.setter
    def RawResponse(cls, newRawResponse):
        cls._rawResponse = newRawResponse
