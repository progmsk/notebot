<?php

class GithubApi {
    private static string $urlTemplate = "https://api.github.com/repos/%s/%s/contents/%s";

    private string $repoOwner;
    private string $repoName;
    private string $accessToken;

    public function __construct(string $repoOwner, string $repoName, string $accessToken)
    {

        $this->repoOwner = $repoOwner;
        $this->repoName = $repoName;
        $this->accessToken = $accessToken;
    }

    private function buildFileUrl(string $filePath) : string {
        return sprintf(
            self::$urlTemplate,
            $this->repoOwner,
            $this->repoName,
            $filePath
        );
    }

    /**
     * @throws Exception
     */
    public function getFileContent(string $filePath) : string {
        $header = [];
        $header[] = "Authorization: token $this->accessToken";
        $header[] = "User-Agent: moscowclub-php-client";
        $curlHandle = curl_init();
        curl_setopt($curlHandle, CURLOPT_URL, $this->buildFileUrl($filePath));
        curl_setopt($curlHandle, CURLOPT_HTTPHEADER, $header);
        curl_setopt($curlHandle, CURLOPT_RETURNTRANSFER, true);

        $response = curl_exec($curlHandle);

        if ($response === false) {
            throw new Exception("CURL failed getting content from github: \n".curl_error($curlHandle));
        }
        curl_close($curlHandle);

        return base64_decode(json_decode($response, true)['content']);
    }
}
