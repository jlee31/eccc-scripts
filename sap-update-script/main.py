import sys
import win32com.client

def connect_to_sap():
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    application = SapGuiAuto.GetScriptingEngine
    connection = application.Children(0)
    session = connection.Children(0)
    return session

def update_description(session, asset_id, lines):
    try: 
        session.findById("wnd[0]").resizeWorkingPane(173, 55, False)
        
        session.findById("wnd[0]/usr/txtTIDNR-LOW").text = asset_id
        session.findById("wnd[0]/usr/txtTIDNR-LOW").setFocus()
        session.findById("wnd[0]/usr/txtTIDNR-LOW").caretPosition = len(asset_id)
        
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        
        shell_control = session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\01/ssubSUB_DATA:SAPLITO0:0102/subSUB_0102A:SAPLITO0:1094/cntlCUST_1094A/shell")
    
        existing_text = shell_control.text  

        new_content = "\n".join(lines)
        updated_text = existing_text + "\n" + new_content
        
        shell_control.text = updated_text
        
        shell_control.setSelectionIndexes(len(updated_text), len(updated_text))

        session.findById("wnd[0]/tbar[0]/btn[11]").press()
    
        return True
        
    except Exception as e:
        print(f"Error updating description: {e}")
        return False

def update_custodian(session, asset_id, custodian_pattern):
    try:
        session.findById("wnd[0]").resizeWorkingPane(173, 55, False)
        session.findById("wnd[0]/usr/txtTIDNR-LOW").text = asset_id
        session.findById("wnd[0]/usr/txtTIDNR-LOW").setFocus()
        session.findById("wnd[0]/usr/txtTIDNR-LOW").caretPosition = len(asset_id)
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        
        session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\02").select()
        
        session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\02/ssubSUB_DATA:SAPLITO0:0102/subSUB_0102C:SAPLITO0:1080/ssubXUSR1080:SAPLXTOB:1000/btnGB_GET_CUST").press()
        session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[3,24]").text = custodian_pattern
        session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[3,24]").setFocus()
        session.findById("wnd[1]/usr/tabsG_SELONETABSTRIP/tabpTAB001/ssubSUBSCR_PRESEL:SAPLSDH4:0220/sub:SAPLSDH4:0220/txtG_SELFLD_TAB-LOW[3,24]").caretPosition = len(custodian_pattern)
        session.findById("wnd[1]").sendVKey(0)
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        
        session.findById("wnd[0]/tbar[0]/btn[11]").press()
        
        try:
            statusbar = session.findById("wnd[0]/sbar")
            message = statusbar.text
            print(f"Asset {asset_id}: {message}")
            
            if "no changes" in message.lower() or "Document was not changed" in message:
                return False
            else:
                return True
        except:
            print(f"Asset {asset_id}: Update completed")
            return True
            
    except Exception as e:
        print(f"Error updating custodian: {e}")
        return None

def update_functional_location(session, asset_id, location):
    try:
        session.findById("wnd[0]").resizeWorkingPane(173, 55, False)
        session.findById("wnd[0]/usr/txtTIDNR-LOW").text = asset_id
        session.findById("wnd[0]/usr/txtTIDNR-LOW").setFocus()
        session.findById("wnd[0]/usr/txtTIDNR-LOW").caretPosition = len(asset_id)
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        
        session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\04").select()
        session.findById("wnd[0]/usr/tabsTABSTRIP/tabpT\\04/ssubSUB_DATA:SAPLITO0:0102/subSUB_0102A:SAPLITO0:1060/subSUB_1060A:SAPLITO0:1065/btnFCODE_CIPL").press()
        session.findById("wnd[1]/tbar[0]/btn[14]").press()
        session.findById("wnd[1]/usr/ctxtIEQINSTALL-TPLNR").text = location
        session.findById("wnd[1]/usr/ctxtIEQINSTALL-TPLNR").caretPosition = len(location)
        session.findById("wnd[1]/tbar[0]/btn[16]").press()
        session.findById("wnd[0]/tbar[0]/btn[11]").press()
        
        return True

    except Exception as e:
        print(f"Error updating functional location: {e}")
        return False
    
def update_status_profile(session, asset_id, profile_row=5):
    try:
        session.findById("wnd[0]").resizeWorkingPane(173, 55, False)
        session.findById("wnd[0]/usr/txtTIDNR-LOW").text = asset_id
        session.findById("wnd[0]/usr/txtTIDNR-LOW").setFocus()
        session.findById("wnd[0]/usr/txtTIDNR-LOW").caretPosition = len(asset_id)
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/usr/subSUB_EQKO:SAPLITO0:0152/subSUB_0152C:SAPLITO0:1526/btn%_AUTOTEXT003").press()
        session.findById(f"wnd[0]/usr/tabsTABSTRIP_0300/tabpANWS/ssubSUBSCREEN:SAPLBSVA:0302/tblSAPLBSVATC_E/radJ_STMAINT-ANWS[0,{profile_row}]").selected = True
        session.findById(f"wnd[0]/usr/tabsTABSTRIP_0300/tabpANWS/ssubSUBSCREEN:SAPLBSVA:0302/tblSAPLBSVATC_E/radJ_STMAINT-ANWS[0,{profile_row}]").setFocus()
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]/tbar[0]/btn[11]").press()
        
        return True
        
    except Exception as e:
        print(f"Error updating status profile: {e}")
        return False

def process_asset(session, asset_id, config):
    if config.get('update_description'):
        lines = config.get('description_lines', [])
        update_description(session=session, asset_id=asset_id, lines=lines)
    
    if config.get('update_custodian'):
        custodian = config.get('custodian_pattern', '')
        update_custodian(session=session, asset_id=asset_id, custodian_pattern=custodian)
    
    if config.get('update_location'):
        location = config.get('functional_location', '')
        update_functional_location(session=session, asset_id=asset_id, location=location)
    
    if config.get('update_status'):
        profile_row = config.get('status_profile_row', 5)
        update_status_profile(session=session, asset_id=asset_id, profile_row=profile_row)
    
    print(f'Processed {asset_id}')

if __name__ == "__main__":
    session = connect_to_sap()
    
    asset_list = [
        "ASSET001",
        "ASSET002",
        "ASSET003"
    ]
    
    configuration = {
        'update_description': True,
        'description_lines': ["Status update - Automated process"],
        'update_custodian': True,
        'custodian_pattern': "DEPARTMENT*",
        'update_location': True,
        'functional_location': "LOCATION-CODE-HERE",
        'update_status': True,
        'status_profile_row': 5
    }
    
    for asset_id in asset_list:
        process_asset(session=session, asset_id=asset_id, config=configuration)
    
    print("All updates completed.")