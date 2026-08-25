import 'package:go_router/go_router.dart';

import '../../features/auth/login_screen.dart';
import '../../features/home/home_screen.dart';
import '../../features/performances/performance_detail_screen.dart';
import '../../features/performances/performances_screen.dart';
import '../../features/performances/record_performance_screen.dart';
import '../../features/routines/routines_screen.dart';

final appRouter = GoRouter(
  initialLocation: '/login',
  routes: [
    GoRoute(path: '/login', builder: (context, state) => const LoginScreen()),
    GoRoute(path: '/home', builder: (context, state) => const HomeScreen()),
    GoRoute(
      path: '/routines',
      builder: (context, state) => const RoutinesScreen(),
    ),
    GoRoute(
      path: '/performances',
      builder: (context, state) => const PerformancesScreen(),
    ),
    GoRoute(
      path: '/performances/record',
      builder: (context, state) => const RecordPerformanceScreen(),
    ),
    GoRoute(
      path: '/performances/:id',
      builder: (context, state) =>
          PerformanceDetailScreen(performanceId: state.pathParameters['id']!),
    ),
  ],
);
