# windows cli : python portconnecormdtov2.py
# 
# to incorporate the original connector authentication md into the v2 connector md
#
# discards the front matter and writes all content after front matter to the target file
#
# manual amends to the created filename where the source filename does not conform to the slugified connector naming convention
import os;
import glob;

md_dict = {
"3DCart":"3dcart",
"access_crm_setup":"access-crm",
"adestra_setup":"adestra",
"Amadeus":"amadeus",
"appdirect-connector":"appdirect",
"aws-ec2":"amazon-ec2",
"aws-s3":"amazon-s3",
"azure_ad_connector_docs":"azure-ad",
"azure-devops-connector":"azure-devops",
"bamboohr_setup":"bamboohr",
"bntouch_docs":"bntouch",
"breathehr":"breathe-hr",
"calendly_setup":"calendly",
"CampusIvy":"campusivy",
"Cardpointe":"cardpointe",
"casavi_setup":"casavi",
"Cavelo":"cavelo",
"chargifyadmin":"chargify",
"choosing_dynamics":"choosing-dynamics",
"clicksend":"clicksend-sms",
"clubready":"club-ready",
"CoinGecko":"coingecko",
"deltek_workbook":"deltek-workbook",
"disciple_media":"disciple-media",
"doc_360_readme":"document-360",
"engagement_multiplier_docs":"engagement-multiplier",
"envision":"envision-salon-spa",
"facebook-marketing":"facebook-marketing-api",
"FluentCommerce":"fluentcommerce",
"Follow-Up-Boss":"follow-up-boss",
"foodtec_docs":"foodtec",
"GoCardless":"gocardless",
"GoDaddy":"godaddy",
"Google_Analytics":"google-analytics",
"google-calendar-workspace":"google-calendar",
"gym_sales":"gym-sales",
"High Level":"high-level",
"infusionsoft_docs":"infusionsoft",
"insider":"insider",
"installing-bronto":"bronto",
"instantco":"instant-co",
"intelliflo_setup_guide":"intelliflo",
"JobNimbus":"jobnimbus",
"jotform_setup":"jotform",
"less_annoying_crm_docs":"less-annoying-crm",
"liana_cms_docs":"liana-cms",
"listrak-rest":"listrak",
"LiveForce":"liveforce",
"magento_2_webhooks":"magento-2-webhooks",
"Mailkit":"mailkit",
"marketo_import_export":"marketo",
"Marketron":"marketron",
"MemoQ":"memoq",
"microsoft_education":"microsoft-education",
"mondaydotcom_setup":"monday-com",
"netsuite_suitetalk_rest_setup":"netsuite-suitetalk",
"openapply_setup":"openapply",
"opencrm_setup":"opencrm",
"petexec_setup":"petexec",
"PhoneBurner":"phoneburner",
"podio_docs":"podio",
"ProfitWell":"profitwell",
"retail_express":"retail-express",
"rockgympro":"rock-gym-pro",
"rybbon_setup_docs":"rybbon",
"sage50":"sage-50",
"sage50cloud":"sage-50-cloud",
"salesforce_chatter":"salesforce-chatter",
"Salesforce_External_ID_Setup":"salesforce-external-id",
"salesforce_marketing_cloud":"salesforce-marketing-cloud",
"salesforce_meta_setup":"salesforce-meta",
"salesforce_pardot":"salesforce-pardot",
"salesforceSoap":"salesforce-soap",
"Salesloft":"salesloft",
"salesnexus_docs":"salesnexus",
"sap_successfactors":"sap-successfactors",
"service_monster_setup":"servicemonster",
"service_now_docs":"servicenow",
"serviceminder":"serviceminder-io",
"shireburn_docs":"shireburn",
"shopify_oauth":"shopify-oauth",
"spark_connector_setup":"spark_membership",
"spotme_docs":"spotme",
"SproutSend":"sprout-send",
"stripe_oauth":"stripe",
"superphone_docs":"superphone",
"tazworks_setup":"tazworks",
"Tenstreet":"tenstreet",
"Totango":"totango",
"trustpilot_readme":"trustpilot",
"twiliovoice":"twilio-voice",
"Unbounce":"unbounce",
"userdotcom_docs":"user-com",
"Velocify":"velocify",
"Vincere":"vincere",
"vonage_docs":"vonage",
"Voucherify":"voucherify",
"Voyado":"voyado",
"xero_oauth20":"xero-oauth20"
}
source_folder = '../../pages/connector-authentication/*.md'
source_folder_full = os.path.join(os.path.dirname(__file__), source_folder)
target_folder = '../../_includes/v2/connector/v1content/'
target_folder_full = os.path.join(os.path.dirname(__file__), target_folder)
for filename in glob.glob(source_folder_full):
	target_file = ''
	md_key = os.path.splitext(os.path.basename(filename))[0]
	# print("Looking for md_dict key "+md_key)
	try:
		target_file = md_dict[md_key]+".md"
	except KeyError:
		target_file = os.path.basename(filename)
	target_file_full = target_folder_full+target_file
	print(filename+" copy to "+target_file_full+"\n")
	with open(filename,'r',encoding="utf8") as fromfile, open(target_file_full,'a') as tofile:
		isfrontmatter = False
		iscontent = False
		for line in fromfile:
			if iscontent == True:
				newline = line
				tofile.write(newline)
			elif line.startswith("---") and isfrontmatter == False:
				isfrontmatter = True
			elif line.startswith("---") and isfrontmatter == True:
				iscontent = True
			else:
				continue
	fromfile.close()
	tofile.close()


