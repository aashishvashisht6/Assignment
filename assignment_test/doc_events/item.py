import frappe
from frappe.utils.safe_exec import get_safe_globals
from frappe.utils import nowdate

def set_custom_fields_values(doc, event=None):
    if doc.get('variant_of'):
        for attr in doc.get('attributes'):
            if attr.attribute in ['Width','Height','Yield']:
                setattr(doc,f"{attr.attribute.lower()}" ,attr.get('attribute_value'))
        
def set_conversion_factor(doc,event=None):
    if doc.get('variant_of'):
        for uom in doc.get('uoms'):
            if uom.formula:
                uom.conversion_factor = frappe.safe_eval(uom.get('formula').strip(), None ,get_context(doc))

def get_context(doc):
	return {
		"doc": doc.as_dict(),
		"nowdate": nowdate,
		"frappe": frappe._dict(utils=get_safe_globals().get("frappe").get("utils")),
	}