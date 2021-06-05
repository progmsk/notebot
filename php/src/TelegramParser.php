<?php


class TelegramParser
{
    public function getCommandFromPayload(string $payload) {

        // /добавитьЗадачу
        $commandText = json_decode($payload)->message->text;

        if (strcmp($commandText, "/добавитьЗадачу") === 0) {
            return new AddTaskCommand("");
        } else {
            throw new Exception("Received unknown command");
        }


    }
}