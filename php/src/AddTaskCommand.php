<?php


class AddTaskCommand
{
    private string $task;

    public function __construct(string $task) {
        $this->task = $task;
    }

    public function getTask() : string {
        return $this->task;
    }
}