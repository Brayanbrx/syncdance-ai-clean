import 'dart:convert';

import 'package:http/http.dart' as http;

import '../config/api_config.dart';

class ApiClient {
  ApiClient({http.Client? client}) : _client = client ?? http.Client();

  final http.Client _client;

  Future<Map<String, dynamic>> get(String path) async {
    final response = await _client.get(Uri.parse('${ApiConfig.baseUrl}$path'));
    if (response.statusCode >= 400) {
      throw http.ClientException(
        'API error ${response.statusCode}',
        response.request?.url,
      );
    }
    return jsonDecode(response.body) as Map<String, dynamic>;
  }
}
