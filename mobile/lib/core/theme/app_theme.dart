import 'package:flutter/material.dart';

abstract final class AppTheme {
  static ThemeData get light => ThemeData(
    colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF7F56D9)),
    useMaterial3: true,
    scaffoldBackgroundColor: const Color(0xFFF8FAFC),
  );
}
