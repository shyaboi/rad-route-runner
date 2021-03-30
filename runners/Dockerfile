FROM ubuntu:latest

# FROM python:latest

# FROM rust:latest

# FROM ruby:latest

# FROM openjdk:8

# FROM node:latest

WORKDIR /app

COPY . .


# Update default packages
RUN apt-get update

# Get Ubuntu packages
RUN apt-get install -y \
    build-essential \
    curl


RUN \
  apt-get update && \
  apt-get install -y ruby

RUN gem install bundler

# RUN yarn install --production

RUN [ruby rubyRunner.rb]