import win32com.client

try:
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    application = SapGuiAuto.GetScriptingEngine
    
    print(f"Connections open: {application.Children.Count}")
    
    if application.Children.Count > 0:
        connection = application.Children(0)  # first connection
        print(f"Sessions in connection: {connection.Children.Count}")
        
        if connection.Children.Count > 0:
            session = connection.Children(0)
            print("Connected to SAP session:", session.Info.SystemName)
        else:
            print("no active connections")
    else:
        print("No SAP connections found.")
        
except Exception as e:
    print("Could not connect")
    print("Error:", e)
