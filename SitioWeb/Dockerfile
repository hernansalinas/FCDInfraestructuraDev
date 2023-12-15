FROM ruby:3.0.2

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8


# Instalar las dependencias necesarias para Jekyll y Just the Docs
RUN apt-get update && apt-get install -y \
  build-essential \
  zlib1g-dev 


WORKDIR /usr/src/app
COPY Gemfile Gemfile.lock ./
#COPY . ./
RUN bundle install
#RUN bundle update
RUN gem install bundler:2.4.22

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--port", "4000"]
