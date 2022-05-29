# Container recipe for Flask Omars api development
FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Install Zsh, Oh my Zsh and other console tools and plugins
RUN apt update && apt install -y git fonts-powerline zsh curl vim less
RUN zsh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k && \
    git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions && \
    git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting && \
    git config --global core.pager 'less -+F' && \
    curl https://gist.githubusercontent.com/dmbarreiro/471a27073f26a7bade6816b873aed1b8/raw/75af38844b41850f70eed2ce2e0587fb492c9b61/.p10k.zsh --output ~/.p10k.zsh && \
    curl https://gist.githubusercontent.com/dmbarreiro/471a27073f26a7bade6816b873aed1b8/raw/75af38844b41850f70eed2ce2e0587fb492c9b61/.zshrc --output ~/.zshrc && \
    chsh -s /bin/zsh

# Install pipenv and project dependencies in /.venv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && \
    pipenv install --dev --system --deploy
