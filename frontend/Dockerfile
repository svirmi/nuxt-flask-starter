FROM node:12

ENV APP_ROOT /src

#RUN mkdir ${APP_ROOT}   #  https://habr.com/ru/post/438862/ check comment
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}

#RUN yarn add nodemon -D && yarn upgrade
RUN yarn build

ENV HOST 0.0.0.0
