from django.http import HttpResponse

def home(request):
    html_file ="""
        <HTML>
        <HEAD>
        <TITLE>Disclaimer</TITLE>
        </HEAD>
        <BODY BGCOLOR="FFFFFF">
        <STYLE>
        a.button {
            -webkit-appearance: button;
            -moz-appearance: button;
            appearance: button;

            text-decoration: none;
            color: initial;
        }
        </STYLE>
        <HR>
        <div align="left"><a href="home" class="button">Home</a></div>
        <div align="center">
        <H1>Copper Questionnaire</H1>
        <H2>Disclaimer</H2>
        <P>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
            mollit anim id est laborum.
        </P></div>
        <HR>
        <div align="right"><a href="rules" class="button">Agree</a></div>
        </BODY>
        </HTML>
    """
    return HttpResponse(html_file)

def rules(request):
    html_file ="""
        <HTML>
        <HEAD>
        <TITLE>rules</TITLE>
        <STYLE>
            a.button {
                -webkit-appearance: button;
                -moz-appearance: button;
                appearance: button;

                text-decoration: none;
                color: initial;
            }
        </STYLE>
        </HEAD>
        <BODY BGCOLOR="FFFFFF">
        <HR>
        <div align="left"><a href="home" class="button">Home</a></div>
        <div align="center">
        <H1>Copper Questionnaire</H1>
        <H2>These are the rules</H2>
        <P>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
            mollit anim id est laborum.
        </P></div>
        <HR>
        <div align="right"><a href="data_visual" class="button">Agree</a></div>
        </BODY>
        </HTML>
    """
    return HttpResponse(html_file)

def thanks(request):
    html_file ="""
        <HTML>
        <HEAD>
        <TITLE>rules</TITLE>
        <STYLE>
            a.button {
                -webkit-appearance: button;
                -moz-appearance: button;
                appearance: button;

                text-decoration: none;
                color: initial;
            }
        </STYLE>
        </HEAD>
        <BODY BGCOLOR="FFFFFF">
        <HR>
        <div align="left"><a href="home" class="button">Home</a></div>
        <div align="center">
        <H1>Copper Questionnaire</H1>
        <H2>Thank you for your participation</H2>
        </div>
        <HR>
        </BODY>
        </HTML>
    """
    return HttpResponse(html_file)
