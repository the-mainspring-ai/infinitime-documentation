xml version="1.0" encoding="utf-8"?





Microsoft Internet Explorer 7.0




# Microsoft Internet Explorer 7.0

ActiveX controls and Scripts are used to enable advanced interaction between the web browser and an application. InfiniTime 7.0 uses ActiveX controls to communicate between the Oracle database and Web browser. By default, most browsers are set to prompt users before allowing ActiveX controls or scripts to be executed. Changing these settings from prompt to enable prevents constant warnings during use of the software.

The following procedures show the steps required to properly configure ActiveX controls and Scripts for the InfiniTime 7.0 software product. Remember, this section is purely informational. The below settings are automatically configured during the InfiniTime 7.0 installation and require no action from the user.

Click on Tools.

![](/img/70InternetOptions.png)

Click on Internet Options to open the Internet Options window for Internet Explorer.

![](/img/70SecurityTab.jpg)

Click on the Security Tab.

![](/img/70InternetOptions.png)

Click on Trusted Sites.

![](/img/ActiveXScrollDown.jpg)

Click Custom Level while Trusted Sites is selected to change the current Internet Security Options for Trusted Sites.

![](/img/AccessDataSourcesAcrossDomains.jpg)

Scroll down through the Security Settings to ActiveX Controls and Plug-ins. Several options are listed below the heading shown in the picture.

![](/img/70Trusted_Sites.jpg)

Enable must be selected for the fifth option âInitialize and script ActiveX controls not marked safeâ.

Enable must also be selected for Access data sources across domains under the miscellaneous heading.

![](/img/AccessDataSourcesAcrossDomains.jpg)

Failing to set these options properly will disable printing from the InfiniTime Software.