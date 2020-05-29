    **ML service based on FLASK** 
    
    this app is a showcase, which makes a linear regression prediction based on 2 quantified features
    the request for the ML prediction shall be maden by a POST request containing a JSON with 2 number (features)
    
    example of the requst:
      curl - i - X POST - H 'Content-Type: application/json' - d '{'params': '4,5'}' localhost:5000/predict
