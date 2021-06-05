<?php

use PHPUnit\Framework\TestCase as TestCase;

final class TelegramParserTest extends TestCase
{
    /**
     * @dataProvider telegramInputProvider
     */
    public function testInterpretCommandToInstance($input, $expectedInstanceType) {
        $parser = new TelegramParser();
        $commandInstance = $parser->getCommandFromPayload($input);

        $this->assertInstanceOf($expectedInstanceType, $commandInstance);
    }

    public function testAddTaskCommandCreated() {
        $telegramPayload = '{"update_id":138656754, "edited_message":{"message_id":18,"from":{"id":666857351,"is_bot":false,"first_name":"\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440","last_name":"\u0420\u043e\u043c\u0430\u043d\u0435\u043d\u043a\u043e","language_code":"ru"},"chat":{"id":666857351,"first_name":"\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440","last_name":"\u0420\u043e\u043c\u0430\u043d\u0435\u043d\u043a\u043e","type":"private"},"date":1622894285,"edit_date":1622897563,"text":"/\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c\u0417\u0430\u0434\u0430\u0447\u0443 \u043d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0442\u0435\u0441\u0442"}}';

        $parser = new TelegramParser();
        $command = $parser->getCommandFromPayload($telegramPayload);

        $this->assertInstanceOf(AddTaskCommand::class, $command);
        $this->assertEquals("написать тест", $command->getTask());
    }

    public function telegramInputProvider() : array {
        return [
            [
                '{"message":{"message_id":18,"from":{"id":666857351,"is_bot":false,"first_name":"\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440","last_name":"\u0420\u043e\u043c\u0430\u043d\u0435\u043d\u043a\u043e","language_code":"ru"},"chat":{"id":666857351,"first_name":"\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440","last_name":"\u0420\u043e\u043c\u0430\u043d\u0435\u043d\u043a\u043e","type":"private"},"date":1622894285,"text":"/\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c\u0417\u0430\u0434\u0430\u0447\u0443"}}',
                 AddTaskCommand::class
            ],
            [
                '{"update_id":138656754, "edited_message":{"message_id":18,"from":{"id":666857351,"is_bot":false,"first_name":"\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440","last_name":"\u0420\u043e\u043c\u0430\u043d\u0435\u043d\u043a\u043e","language_code":"ru"},"chat":{"id":666857351,"first_name":"\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440","last_name":"\u0420\u043e\u043c\u0430\u043d\u0435\u043d\u043a\u043e","type":"private"},"date":1622894285,"edit_date":1622897563,"text":"/\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c\u0417\u0430\u0434\u0430\u0447\u0443 \u043d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0442\u0435\u0441\u0442"}}',
                AddTaskCommand::class
            ]
        ];
    }
}