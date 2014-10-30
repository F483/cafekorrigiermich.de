# cafekorrigiermich.de

## Installation for development

    # Clone repository
    cd where/you/keep/your/repos
    git clone https://github.com/F483/cafekorrigiermich.de
    cd cafekorrigiermich.de

    # setup python virtualenv
    virtualenv -p /usr/bin/python2 env  # create virtualenv
    source env/bin/activate             # activate virtualenv

    # install python packages
    pip install pelican
    pip install Markdown

    # basic useage
    make html       # compile static site
    make serve      # start development server
    make ssh_upload # upload to server
