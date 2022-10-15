import rpa as r

r.init(visual_automation=True)

r.url("http://www.talentcards.com/login")
r.type('//*[@id="frm_s1"]', "jmbenedetto@byhumane.com")
r.type('//*[@id="frm_s2"]', "smep_spal5CAC-nink")
r.click('//*[@id="submit-button-login"]')

r.click('//*[@id="vuetify-app"]/div/header/div[1]/a[4]')
r.click('//*[@id="root"]/div/div/div/span/div/div[1]/div/div/div[1]/button')
# r.click('//*[@id="vuetify-app"]/div/main/div/div[3]/div[2]')
r.click("//div[@class='toast toast-success']")
r.close()
