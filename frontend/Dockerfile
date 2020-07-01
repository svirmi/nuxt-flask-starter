FROM node:12

ENV APP_ROOT /src

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}

RUN yarn && yarn upgrade
RUN yarn build

ENV HOST 0.0.0.0
